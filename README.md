# repract2018
Data Analysis for the 2018 Edition of the RE-Pract Survey

Final Data in the folder `data/codedtruth` (csv headers explained): 
- `truth_metadata.csv`: lfdn plus all respondent metadata with coded/integrated columns for `v_5/v_6`, `v_15/v_16`, `v_11` and `v_19` appended (for aggregation of ratings over respondent metadata)
- `truth_overflow.csv`: lfdn,`v_18`,`v_1373` (variables yet to code)
- `truth_ratings.csv`: lfdn,PaperID,rating (ordinal ratings)
- `v_8345etseq_final.csv`: PaperID,lfdn,reasoning,Tag (positive reasoning)
- `v_8780etseq_final.csv`: PaperID,lfdn,reasoning,Tag (negative reasoning)
- `papertags_how_withwhom_final`: PaperID,PaperSummary,Tag (how and with whom tags for aggregation of ratings over papers)
- `papertags_what_final`: PaperID,PaperSummary,Tag (what tags for aggregation of ratings over papers)
The rest of the `_final` files in the folder are helper files (integrated in the files explained above).

These files were generated in `documentation/response_integration_notebooks` (because it was close to the validated used in the process).
The work in `analysis` is based on the preliminary data. 
Notebooks based on the truth data will be put in a `truth` folder inside the `notebooks` folder, not sure where I'll put the helpers or results yet. 
Sorry for the folder mess.