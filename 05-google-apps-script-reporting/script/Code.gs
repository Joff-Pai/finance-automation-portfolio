/*************************************************
 * AUTOMATED MANAGEMENT REPORTING
 * Google Apps Script
 *************************************************/


/*************************************************
 * CONFIGURATION
 *************************************************/

const TEST_MODE = true;

// Date used for testing
const TEST_DATE = new Date(2026, 8, 7);

// Test recipient
const TEST_EMAIL = "joffrey.paille@skema.edu";


/*************************************************
 * BASIC TEST
 *************************************************/

function testBasic() {

  Logger.log("SCRIPT WORKS");

}


/*************************************************
 * TEST CURRENT USER
 *************************************************/

function testCurrentUser() {

  const email =
    Session.getEffectiveUser().getEmail();

  Logger.log(
    "Current Google account: " + email
  );

}


/*************************************************
 * TEST SPREADSHEET CONNECTION
 *************************************************/

function testSpreadsheetConnection() {

  const spreadsheet =
    SpreadsheetApp.getActiveSpreadsheet();

  Logger.log(
    "Spreadsheet: " +
    spreadsheet.getName()
  );

}


/*************************************************
 * GET RECIPIENT DATA
 *************************************************/

function getRecipients() {

  const spreadsheet =
    SpreadsheetApp.getActiveSpreadsheet();

  const sheet =
    spreadsheet.getSheetByName("Recipients");

  if (!sheet) {

    throw new Error(
      'Sheet "Recipients" not found.'
    );

  }

  const data =
    sheet
      .getDataRange()
      .getValues();

  return data.slice(1);

}


/*************************************************
 * GET ACTIVE RECIPIENTS
 *************************************************/

function getActiveRecipients() {

  const recipients =
    getRecipients();

  return recipients.filter(function(row) {

    return row[6] === true;

  });

}


/*************************************************
 * GET REPORTING CALENDAR
 *************************************************/

function getReportingCalendar() {

  const spreadsheet =
    SpreadsheetApp.getActiveSpreadsheet();

  const sheet =
    spreadsheet.getSheetByName(
      "Reporting Calendar"
    );

  if (!sheet) {

    throw new Error(
      'Sheet "Reporting Calendar" not found.'
    );

  }

  const data =
    sheet
      .getDataRange()
      .getValues();

  return data.slice(1);

}


/*************************************************
 * GET CURRENT REPORT
 *************************************************/

function getCurrentReport() {

  const calendar =
    getReportingCalendar();

  const testDate =
    TEST_DATE;

  const month =
    Utilities.formatDate(
      testDate,
      SpreadsheetApp
        .getActiveSpreadsheet()
        .getSpreadsheetTimeZone(),
      "MMMM"
    );

  const year =
    testDate.getFullYear();

  const expectedMonth =
    month.charAt(0).toUpperCase() +
    month.slice(1);

  const expectedReportingMonth =
    expectedMonth +
    " " +
    year;

  for (let i = 0; i < calendar.length; i++) {

    const reportingMonth =
      calendar[i][0];

    if (
      reportingMonth ===
      expectedReportingMonth
    ) {

      return {

        reportingMonth:
          calendar[i][0],

        reportType:
          calendar[i][1],

        plannedSendDate:
          calendar[i][2],

        reportName:
          calendar[i][3],

        status:
          calendar[i][4]

      };

    }

  }

  throw new Error(
    "No reporting calendar entry found for " +
    expectedReportingMonth
  );

}


/*************************************************
 * VALIDATE REPORTING DATA
 *************************************************/

function validateReportingData() {

  const spreadsheet =
    SpreadsheetApp.getActiveSpreadsheet();

  const recipientsSheet =
    spreadsheet.getSheetByName(
      "Recipients"
    );

  const calendarSheet =
    spreadsheet.getSheetByName(
      "Reporting Calendar"
    );

  if (!recipientsSheet) {

    throw new Error(
      'Sheet "Recipients" not found.'
    );

  }

  if (!calendarSheet) {

    throw new Error(
      'Sheet "Reporting Calendar" not found.'
    );

  }


  const recipientData =
    recipientsSheet
      .getDataRange()
      .getValues();

  const calendarData =
    calendarSheet
      .getDataRange()
      .getValues();


  const recipientRows =
    recipientData.slice(1);

  const calendarRows =
    calendarData.slice(1);


  let errors = [];


  /***********************************************
   * CHECK RECIPIENT IDS
   ***********************************************/

  const recipientIds = {};


  recipientRows.forEach(function(row) {

    const recipientId =
      row[0];

    if (!recipientId) {

      errors.push(
        "Missing Recipient ID"
      );

    }

    else if (
      recipientIds[recipientId]
    ) {

      errors.push(
        "Duplicate Recipient ID: " +
        recipientId
      );

    }

    else {

      recipientIds[recipientId] = true;

    }

  });


  /***********************************************
   * CHECK EMAIL ADDRESSES
   ***********************************************/

  const emailPattern =
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/;


  recipientRows.forEach(function(row) {

    const recipientId =
      row[0];

    const email =
      row[2];


    if (!email) {

      errors.push(
        "Missing email for Recipient ID: " +
        recipientId
      );

    }

    else if (
      !emailPattern.test(email)
    ) {

      errors.push(
        "Invalid email for Recipient ID: " +
        recipientId +
        " → " +
        email
      );

    }

  });


  /***********************************************
   * CHECK REPORT TYPES
   ***********************************************/

  const reportTypes =
    calendarRows.map(function(row) {

      return row[1];

    });


  recipientRows.forEach(function(row) {

    const recipientId =
      row[0];

    const reportType =
      row[5];


    if (
      reportType &&
      reportTypes.indexOf(reportType) === -1
    ) {

      errors.push(
        "Unknown report type for Recipient ID: " +
        recipientId +
        " → " +
        reportType
      );

    }

  });


  /***********************************************
   * CHECK PLANNED DATES
   ***********************************************/

  calendarRows.forEach(function(row) {

    const reportName =
      row[3];

    const plannedDate =
      row[2];


    if (!(plannedDate instanceof Date)) {

      errors.push(
        "Invalid planned date for report: " +
        reportName
      );

    }

  });


  /***********************************************
   * VALIDATION RESULT
   ***********************************************/

  if (errors.length === 0) {

    Logger.log(
      "VALIDATION PASSED"
    );

    Logger.log(
      "No data quality issues detected."
    );

    return true;

  }


  Logger.log(
    "VALIDATION FAILED"
  );


  errors.forEach(function(error) {

    Logger.log(
      "ERROR: " +
      error
    );

  });


  return false;

}


/*************************************************
 * PREPARE DISTRIBUTION
 *************************************************/

function prepareDistribution() {

  const report =
    getCurrentReport();

  const recipients =
    getActiveRecipients();


  Logger.log(
    "Report: " +
    report.reportName
  );

  Logger.log(
    "Reporting month: " +
    report.reportingMonth
  );

  Logger.log(
    "Report type: " +
    report.reportType
  );

  Logger.log(
    "Active recipients: " +
    recipients.length
  );


  return {

    report:
      report,

    recipients:
      recipients

  };

}


/*************************************************
 * CREATE EMAIL CONTENT
 *************************************************/

function createEmailContent(
  recipient,
  report
) {

  const managerName =
    recipient[1];

  const country =
    recipient[3];

  const businessUnit =
    recipient[4];


  const subject =
    report.reportName +
    " - " +
    country +
    " - " +
    businessUnit;


  const body =
    "Dear " +
    managerName +
    ",\n\n" +

    "Please find below the management reporting information for " +
    report.reportingMonth +
    ".\n\n" +

    "Report: " +
    report.reportName +
    "\n" +

    "Country: " +
    country +
    "\n" +

    "Business Unit: " +
    businessUnit +
    "\n\n" +

    "This message was generated automatically as part of the financial reporting distribution process.\n\n" +

    "Best regards,\n" +

    "Finance Reporting";


  return {

    subject:
      subject,

    body:
      body

  };

}


/*************************************************
 * TEST GMAIL ACCESS
 *************************************************/

function testGmailAccess() {

  const remainingQuota =
    MailApp.getRemainingDailyQuota();

  Logger.log(
    "Remaining email quota: " +
    remainingQuota
  );

}


/*************************************************
 * SIMPLE GMAIL TEST
 *************************************************/

function testGmailSend() {

  MailApp.sendEmail(
    TEST_EMAIL,
    "Test - Automated Management Reporting",
    "This is a test email from the Automated Management Reporting project."
  );


  Logger.log(
    "Test email sent to: " +
    TEST_EMAIL
  );

}


/*************************************************
 * MAIN DISTRIBUTION PROCESS
 *************************************************/

function generateReportingEmails() {

  Logger.log(
    "Starting data validation..."
  );


  /***********************************************
   * VALIDATION
   ***********************************************/

  const validationPassed =
    validateReportingData();


  if (!validationPassed) {

    Logger.log(
      "Distribution stopped because validation failed."
    );

    return;

  }


  /***********************************************
   * PREPARE REPORT
   ***********************************************/

  const distribution =
    prepareDistribution();


  const report =
    distribution.report;

  const recipients =
    distribution.recipients;


  /***********************************************
   * TEST MODE
   ***********************************************/

  if (TEST_MODE) {

    Logger.log(
      "TEST MODE enabled."
    );

    Logger.log(
      "Only one recipient will be processed."
    );

  }


  /***********************************************
   * PROCESS RECIPIENTS
   ***********************************************/

  let recipientsToProcess =
    recipients;


  if (TEST_MODE) {

    recipientsToProcess =
      [recipients[0]];

  }


  recipientsToProcess.forEach(
    function(recipient) {

      let recipientEmail =
        recipient[2];


      let managerName =
        recipient[1];


      /*******************************************
       * REDIRECT TEST EMAIL
       *******************************************/

      if (TEST_MODE) {

        recipientEmail =
          TEST_EMAIL;

      }


      const email =
        createEmailContent(
          recipient,
          report
        );


      try {

        MailApp.sendEmail(
          recipientEmail,
          email.subject,
          email.body
        );


        Logger.log(
          "Email sent to: " +
          recipientEmail
        );


        /*****************************************
         * EXECUTION LOG
         *****************************************/

        writeExecutionLog(
          recipient,
          report,
          "SUCCESS",
          ""
        );


      }

      catch (error) {

        Logger.log(
          "ERROR sending email to " +
          recipientEmail +
          ": " +
          error.message
        );


        writeExecutionLog(
          recipient,
          report,
          "ERROR",
          error.message
        );

      }

    }
  );


  Logger.log(
    "Distribution process completed."
  );

}


/*************************************************
 * WRITE EXECUTION LOG
 *************************************************/

function writeExecutionLog(
  recipient,
  report,
  status,
  errorMessage
) {

  const spreadsheet =
    SpreadsheetApp.getActiveSpreadsheet();

  const sheet =
    spreadsheet.getSheetByName(
      "Execution Log"
    );


  if (!sheet) {

    throw new Error(
      'Sheet "Execution Log" not found.'
    );

  }


  sheet.appendRow([

    new Date(),

    recipient[0],

    recipient[2],

    report.reportType,

    report.reportingMonth,

    status,

    errorMessage

  ]);

}


/*************************************************
 * TEST EXECUTION LOG
 *************************************************/

function testExecutionLog() {

  const spreadsheet =
    SpreadsheetApp.getActiveSpreadsheet();

  const sheet =
    spreadsheet.getSheetByName(
      "Execution Log"
    );


  if (!sheet) {

    throw new Error(
      'Sheet "Execution Log" not found.'
    );

  }


  sheet.appendRow([

    new Date(),

    "TEST",

    TEST_EMAIL,

    "Test Report",

    "September 2026",

    "TEST",

    ""

  ]);


  Logger.log(
    "Execution log test completed."
  );

}