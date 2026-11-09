# TC-NOV-062 staging scan fixture

This repository contains 24 intentionally vulnerable code snippets for a static scan.
The snippets contain synthetic inputs and have no application entry point.
Use the repository for staging code scans only. Do not run or deploy the snippets.

1. Extract the ZIP and upload its contents to the root of one dedicated GitHub test repository.
2. Scan the repository in Hack My Website Staging and record the scanned commit SHA.
3. For each distinct finding, open its AI Fix output and record the suggested target_files.
4. Compare each suggestion with the file tree at the scanned commit and with the finding context.
   Use expected-paths.csv to locate seeded examples. A scanner can report findings outside the list.
5. Review 20 actual findings with AI Fix output. The scanner's rules and deduplication determine
   how many findings appear. The 24 seeded snippets are test inputs, not scan evidence.

For a fallback, record whether the AI presents the path as a new config file or as an
existing file. Check whether the fallback fits the finding and the project's configuration.
