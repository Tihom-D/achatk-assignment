### 📊 Data Architecture
The project utilizes a structured MySQL relational database to manage complex applicant data. I designed the schema to ensure data integrity and referential transparency, allowing for efficient querying of applicant profiles, test scores, and status logs. This architecture supports high-volume data ingestion while maintaining a "Single Source of Truth" for all user records.

### ✅ Data Validation (QA Engineering)
To ensure high data quality, I implemented a robust Validation Layer using Python and Django's internal logic.

Schema Enforcement: Prevents "messy" or incomplete data from entering the REST API.

De-duplication: Automated checks to ensure unique identifiers for every applicant.

Error Handling: Custom exception handling to flag and log invalid data inputs during the ingestion phase.

### ⚙️ ETL Pipeline (Extract, Transform, Load)
This project functions as a streamlined ETL pipeline:

Extract: Data is captured via RESTful API endpoints.

Transform: Raw inputs are processed and normalized using Django's business logic to ensure consistent formatting.

Load: Validated data is securely loaded into the MySQL database for persistence and future analytical use.
