# budget
A small program I made to help manage my budget and see my spendings clearer.

## How it Works

It takes in a file of transactions and users are able to classify each transaction as a category (e.g. Food, Transport). User input consists of the category followed by a phrase to identify future transactions. 

### Example

data.txt:
```
Date,Amount,Description
11/05/2019,-20,PURCHASE AUTHORIZED ON 11/01 DEL TACO...
11/05/2019,-10,PURCHASE AUTHORIZED ON 11/01 IN N OUT...
11/06/2019,-10,PURCHASE AUTHORIZED ON 11/02 TACO BELL...
```

Categories.txt:
```
Food
Transportation
```

The whole run on the console will look like this (where user input are between the '<' and '>'):
```
1 : Food
2 : Transportation

$20 PURCHASE AUTHORIZED ON 11/01 DEL TACO...
Category #: <1 TACO>

1 : Food
2 : Transportation

$10 PURCHASE AUTHORIZED ON 11/01 IN N OUT...
Category #: <1 IN N OUT>
$10 PURCHASE AUTHORIZED ON 11/02 TACO BELL... (Food)
```

Notice that on the last entry, the program does not ask for input, this is because it records that all descriptions with 'TACO' in it will be categorized to 1, which is Food. The user may also leave the phrase blank, in which there will be no phrase recorded.

The resulting output files would be : 
- Food.txt (key phrases to classify to Food, in this case the only non-whitespace line will contain TACO)
- Transportation.txt (key phrases to classify to Transportation, which will be blank)
- Budget.txt (List out all the classified items according to the categories)
- Daily.csv (spreadsheet of the daily spendings according to categories)
- Monthly.csv (spreadsheet of the monthly spendings according to categories)

The user may choose to type in STOP to stop the program in the middle and saving the progress to the files (but not changing the data.txt file). The next time the user runs the program, it will use the saved key phrases to re-sort the data from the beginning.

## Usage

Run in Python3! 

The program will take in and output several text files. It will classify each transaction into several categories. The base requirement is to make 2 input files in the same directory as the program: data.txt and Categories.txt.

From the data you have, make a comma-delimited file (can initially be a csv file) named data.txt. The format is for data.txt should be:
- Header on first row
- 3 Columns: 
  * Date (MM/DD/YYYY)
  * Amount (floats possible, negative for money out)
  * Transaction Description
- Sorted in Ascending/Descinding order (as long as it is ordered)

Place your data.txt file in the same directory as the program.

Secondly, you should make a Categories.txt file which consists of the categories you wish to have it sorted to. Format should be:
- One category per line
- Case Sensitive
