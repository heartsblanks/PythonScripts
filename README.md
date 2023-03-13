<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="xml" indent="yes"/>
  <xsl:template match="/">
    <xsl:apply-templates select="//xsd:element"/>
  </xsl:template>
  <xsl:template match="xsd:element">
    <xsl:element name="{@name}">
      <xsl:attribute name="type">
        <xsl:value-of select="@type"/>
      </xsl:attribute>
      <xsl:attribute name="minOccurs">
        <xsl:value-of select="@minOccurs"/>
      </xsl:attribute>
      <xsl:attribute name="maxOccurs">
        <xsl:value-of select="@maxOccurs"/>
      </xsl:attribute>
      <xsl:apply-templates select="xsd:annotation"/>
      <xsl:apply-templates select="xsd:complexType"/>
    </xsl:element>
  </xsl:template>
  <xsl:template match="xsd:annotation">
    <xsl:element name="annotation">
      <xsl:apply-templates select="xsd:documentation"/>
    </xsl:element>
  </xsl:template>
  <xsl:template match="xsd:documentation">
    <xsl:element name="documentation">
      <xsl:value-of select="."/>
    </xsl:element>
  </xsl:template>
</xsl:stylesheet>
