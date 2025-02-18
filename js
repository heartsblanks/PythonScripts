<script>
function toggleFields() {
    var env = document.querySelector("select[name='ENVIRONMENT']").value;
    var jiraTaskField = document.querySelector("input[name='JIRA_TASK']").closest("tr");
    var changeRequestField = document.querySelector("input[name='CHANGE_REQUEST']").closest("tr");

    if (env === "UAT") {
        jiraTaskField.style.display = "";
        changeRequestField.style.display = "none";
    } else if (env === "PROD") {
        jiraTaskField.style.display = "none";
        changeRequestField.style.display = "";
    } else {
        jiraTaskField.style.display = "none";
        changeRequestField.style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    toggleFields();
    document.querySelector("select[name='ENVIRONMENT']").addEventListener("change", toggleFields);
});
</script>