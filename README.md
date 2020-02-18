# repract2018

This project constitutes a large collaboration lead by Xavier Franch, Daniel Mendez, and Andreas Vogelsang. The project constitutes a survey which aims at exploring the perceived relevance of surveyed practitioners on RE-related publications from past years.

The repository includes the material from the survey to increase transparency and support reproducibilty of our findings.

* The folder `analysis` includes the results of the qualitative and quantitative analyses. 
* The folder `notebooks` includes the jupyter notebooks used for the respective analyses. 
* The main data set is in the folder `data/codedtruth` (csv headers explained):
  - `truth_metadata.csv`: lfdn plus all respondent metadata with coded/integrated columns for `v_5/v_6`, `v_15/v_16`, `v_11` and `v_19` appended (for aggregation of ratings over respondent metadata)
  - `truth_overflow.csv`: lfdn,`v_18`,`v_1373` (variables yet to code)
  - `truth_ratings.csv`: lfdn,PaperID,rating (ordinal ratings)
  - `v_8345etseq_final.csv`: PaperID,lfdn,reasoning,Tag (positive reasoning)
  - `v_8780etseq_final.csv`: PaperID,lfdn,reasoning,Tag (negative reasoning)
  - `papertags_how_withwhom_final`: PaperID,PaperSummary,Tag (how and with whom tags for aggregation of ratings over papers)
  - `papertags_what_final`: PaperID,PaperSummary,Tag (what tags for aggregation of ratings over papers)
  - The rest of the `_final` files in the folder are helper files (integrated in the files explained above). Additional files on selected variables can be found under the respective `dataexports` folder.

