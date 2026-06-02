from selenium import webdriver

driver = webdriver.Chrome()

# Create HTML Report
report = open("TestReport.html", "w")

report.write("<html><body>")
report.write("<h1>Selenium Test Report</h1>")
report.write("<table border='1'>")
report.write("<tr><th>Test Case</th><th>Status</th></tr>")

try:
    
    driver.get("https://www.google.com")

    expected_title = "Google"
    actual_title = driver.title

    if expected_title == actual_title:
        
        report.write("<tr>")
        report.write("<td>Google Title Verification</td>")
        report.write("<td style='color:green'>PASS</td>")
        report.write("</tr>")

    else:
        
        report.write("<tr>")
        report.write("<td>Google Title Verification</td>")
        report.write("<td style='color:red'>FAIL</td>")
        report.write("</tr>")

except Exception as e:

    report.write("<tr>")
    report.write("<td>Google Title Verification</td>")
    report.write("<td style='color:red'>ERROR</td>")
    report.write("</tr>")

finally:

    report.write("</table>")
    report.write("</body></html>")

    report.close()
    driver.quit()