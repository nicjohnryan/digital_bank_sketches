
#========================
# Jaro Winkler in R
#========================

library(RecordLinkage)
library(dplyr)
library(stringdist)

ref <- c('Wages ABC Pty Ltd SEP')
words <- c('Wages ABC Pty Ltd JUN', 'Wages ABC Pty Ltd JUL', 'Wages ABC Pty Ltd AUG',
           'UBER Some Random Town 56437', 'Ice Cream Shop random digits 23456', 'Ice Cream Shop random digits 23456') 

ref <- toupper(words)
words <- toupper(words)

jw_data_input <- expand.grid(words = words, ref = ref, stringsAsFactors = FALSE)
jw_data_output <- jw_data_input %>% 
                        group_by(words) %>% 
                        mutate(match_score = 1-stringdist(words, ref, method="jw")) 

# typical bimodal distribution
hist(jw_data_output$match_score, 
        main="Jaro Winkler Scores", 
        col="pink",
        xlab="match score")


    