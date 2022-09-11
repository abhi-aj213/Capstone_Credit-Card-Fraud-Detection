# Capstone_Credit-Card-Fraud-Detection
Objective: Create system to identify/detect Credit Card Fraud, Ingest data using Apache Sqoop , process the streaming data and make Real-time decisions Solution: Load data in No Sql , Ingest data using AWS RDS ,Create look up tables , Created streaming framework for real time data  Key Achievement: Loaded Data and Created Look up tables , Created a streaming data processing framework that ingests real-time POS transaction data from Kafka, Validation system from Fraud detection

As part of the project, broadly, you are required to perform the following tasks:

Task 1: Load the transactions history data (card_transactions.csv) in a NoSQL database.

Task 2: Ingest the relevant data from AWS RDS to Hadoop.

Task 3: Create a look-up table with columns specified earlier in the problem statement.

Task 4: After creating the table, you need to load the relevant data in the lookup table.

Task 5: Create a streaming data processing framework that ingests real-time POS transaction data from Kafka. The transaction data is then validated based on the three rules’ parameters (stored in the NoSQL database) discussed previously.

Task 6: Update the transactions data along with the status (fraud/genuine) in the card_transactions table.

Task 7: Store the ‘postcode’ and ‘transaction_dt’ of the current transaction in the look-up table in the NoSQL database if the transaction was classified as genuine.

![image](https://user-images.githubusercontent.com/55485987/189535385-22f4a9ff-95a6-4a27-8735-64c232f6078f.png)
