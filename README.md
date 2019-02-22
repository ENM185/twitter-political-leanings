# Simple Neural Network

 - Stored in `simple` branch
 - First, a list of senators was created on Twitter
   - Multiple Twitter handles were included per politician if available, as long as they were verified accounts
   - Stored in `politicians/politicians.json`
     - Political party listed, along with Twitter handle
 - From this list, the most common words were received
   - Max of 100 Tweets per handle
   - Does not include "stop words" (common words such as 'the' or 'an')
   - Words were deleted by hand that had symbols or are too common/unrelated to politics
   - Stored as list in `common_words/words.json`
 - Training data was generated using these common words
   - Again, a max of 100 Tweets were used per handle
   - An array was created for each Tweet with a `1` indicating the common word was found, and `0` indicating otherwise
     - Same order as `common_words/words.json`
   - Arrays that contained 5+ of the common words were stored in `dataset/data.json`
     - Classified under `Republicans` or `Democrats` (based on user's party)