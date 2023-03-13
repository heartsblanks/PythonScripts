import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.ibm.broker.config.proxy.BrokerProxy;
import com.ibm.broker.config.proxy.ConfigurableService;
import com.ibm.broker.config.proxy.ConfigurableServiceProxy;
import com.ibm.broker.config.proxy.ConfigurableServiceType;
import com.ibm.broker.config.proxy.DeployableObject;
import com.ibm.broker.config.proxy.MessageFlowProxy;
import com.ibm.broker.config.proxy.MessageSetProxy;
import com.ibm.broker.config.proxy.MessageTypeProxy;
import com.ibm.broker.config.proxy.RecordedOutputNodeProxy;
import com.ibm.broker.config.proxy.RecordedOutputTerminalProxy;
import com.ibm.broker.config.proxy.RecordedOutputTerminalSetProxy;
import com.ibm.broker.config.proxy.SchemaProxy;
import com.ibm.broker.config.proxy.SchemaTypeProxy;
import com.ibm.broker.config.proxy.SubFlowProxy;
import com.ibm.broker.config.proxy.SubFlowProxyReference;
import com.ibm.broker.config.proxy.TopicProxy;
import com.ibm.broker.config.proxy.TopicSpaceProxy;

public class IIB10MessageSetToDfdlConverter {
    
    // Set the path to the message set project directory
    private static final String MESSAGE_SET_DIR = "/path/to/message/set/project";
    
    // Set the path to the DFDL schema output directory
    private static final String DFDL_DIR = "/path/to/dfdl/schema/output";
    
    // Set the name of the message set project
    private static final String MESSAGE_SET_NAME = "MyMessageSet";
    
    // Set the name of the output DFDL message model
    private static final String DFDL_NAME = "MyDfdlModel";
    
    public static void main(String[] args) {
        try {
            // Connect to the local broker
            BrokerProxy brokerProxy = BrokerProxy.getLocalInstance();
            
            // Load the message set project
            MessageSetProxy messageSetProxy = brokerProxy.getMessageSetByName(MESSAGE_SET_NAME, MESSAGE_SET_DIR);
            
            // Create a new DFDL schema
            SchemaProxy dfdlSchemaProxy = brokerProxy.createSchema(DFDL_NAME, DFDL_DIR);
            
            // Iterate through the message types in the message set project and add them to the DFDL schema
            for (MessageTypeProxy messageTypeProxy : messageSetProxy.getMessageTypes()) {
                SchemaTypeProxy schemaTypeProxy = brokerProxy.createSchemaType(messageTypeProxy.getName());
                
                // Iterate through the message type fields and add them to the DFDL schema type
                for (RecordedOutputNodeProxy recordedOutputNodeProxy : messageTypeProxy.getRecordedOutputNodes()) {
                    if (recordedOutputNodeProxy.getTerminalSet() != null) {
                        RecordedOutputTerminalSetProxy recordedOutputTerminalSetProxy = recordedOutputNodeProxy.getTerminalSet();
                        List<RecordedOutputTerminalProxy> recordedOutputTerminalProxies = new ArrayList<RecordedOutputTerminalProxy>();
                        recordedOutputTerminalSetProxy.copyTo(recordedOutputTerminalProxies);
                        
                        for (RecordedOutputTerminalProxy recordedOutputTerminalProxy : recordedOutputTerminalProxies) {
                            if (recordedOutputTerminalProxy.getSchemaType() != null) {
                                SchemaTypeProxy childSchemaTypeProxy = brokerProxy.createSchemaType(recordedOutputTerminalProxy.getSchemaType().getName());
                                schemaTypeProxy.addTypeReference(recordedOutputTerminalProxy.getName(), childSchemaTypeProxy, recordedOutputTerminalProxy.getCardinality().toString());
                            } else if (recordedOutputTerminalProxy.getMessageType() != null) {
                               
                            MessageTypeProxy childMessageTypeProxy = recordedOutputTerminalProxy.getMessageType();
                            SchemaTypeProxy childSchemaTypeProxy = brokerProxy.createSchemaType(childMessageTypeProxy.getName());
                            schemaTypeProxy.addTypeReference(recordedOutputTerminalProxy.getName(), childSchemaTypeProxy, recordedOutputTerminalProxy.getCardinality().toString());
                        } else {
                            // If the recorded output terminal is not associated with a schema type or message type, 
                            // add it as a simple field with a default data type of xs:string
                            schemaTypeProxy.addField(recordedOutputTerminalProxy.getName(), "xs:string", recordedOutputTerminalProxy.getCardinality().toString());
                        }
                    }
                } else {
                    // If the recorded output node does not have a terminal set, add it as a simple field with a default data type of xs:string
                    schemaTypeProxy.addField(recordedOutputNodeProxy.getName(), "xs:string", "1");
                }
            }
            
            // Add the schema type to the DFDL schema
            dfdlSchemaProxy.addSchemaType(schemaTypeProxy);
        }
        
        // Save the DFDL schema to a file
        File dfdlFile = new File(DFDL_DIR, DFDL_NAME + ".xsd");
        FileWriter writer = new FileWriter(dfdlFile);
        writer.write(dfdlSchemaProxy.toXSDString());
        writer.close();
        
        System.out.println("DFDL schema created: " + dfdlFile.getAbsolutePath());
    } catch (IOException e) {
        e.printStackTrace();
    } catch (Exception e) {
        e.printStackTrace();
    }
}
