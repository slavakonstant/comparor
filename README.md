Author: Slava Konstant
Date: 10/6/2020
Objective: The purpose of this package is to compare two documents containing
  text to determine if they are similar.  Based on the requirement, there has
  been a bit of ambiguity of specific need.  Hence, the following logic is used:
  a. If the two documents are exactly the same, application returns "1" via
  system exit/return value for API.
  b. If the two files are not identical, we shall utilize a metric to find a similarity.
  Algorithm:
    1. Ignore commonly used, case insensitive words in "stop_words.txt".  This file
      may be updated, if needed.
    2. Define MATCHING_THRESHOLD as percentage, currently set to 70%, to compare
    if the two documents are similar.  Any word in document A that exists in document B
    time shall be considered.  Next, for a given word, if the occurrence count is
    equal or above MATCHING_THRESHOLD %, we shall count the word as a match.  If total
    matched words out of the largest document A or B is above MATCHING_THRESHOLD %,
    we shall deem the two documents similar enough, and treat this case
    same as (a) above, and return "1" via system exit/return value for API.
  c. If two documents don’t have ANY words in common, application returns "0".


Installation Instructions:
-- Pre-requite:
  1. Python: to install visit: https://www.python.org/downloads/ and download
    and install Python per your operating system type.
-- Runing:
  1. Get the package from repo: https://github.com/slavakonstant/comparor.git
  1. Define files to compare under: <application folder>/test/data/
    file_a, file_b.  Note: sample files are included: s1, s2, and s3.
  2. Open command/terminal, and execute via:
    python comparer.py <file_a> <file_b>  

    Note: specify the file location under the <application folder>/test/data path,
    For example:
      python comparer.py test/data/s1 test/data/s2

Additional support: web application, "app.py", REST API has been created to respond to POST
  request under root (/).  To test processing POST requests:
  1. Start the server: python app.py
  2. Send POST using curl, or the supplied helper function in
    /test/rest_load.py to simulate POST requests.
