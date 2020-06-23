<img src="logo.svg" width=155 height=155 align="right">

## Salary Bias in Tech

After seeing yet another [tech demo](https://github.com/scailable/sclbl-tutorials/issues/7) that involved sexism I figured it would be good to investigate a dataset on salary bias. I got tired of seeing the "Just Another Dangerous Situation"-theme happening and decided it would be good to explore the topic properly. 

## Data 

The data used in this research can be found [here](https://insights.stackoverflow.com/survey/). We've used the 2019 data and placed the `survey_results_public.csv` file in the data folder of this project. 

## Goal 

There's a few goals I have in mind.

1. I'd like to measure the effect of gender on salary, correcting for jobtitle, country and programming experience.
2. I'd like to measure the effect of ethnicity on salary, correcting for jobtitle, country and programming experience.
3. I'd like to measure how (and frankly if at all) fairness mitigation techniques remedy any bias. Both in the dataset as well as in the model.

For me personally I hope to write a blogpost on the lessons from this exercise and anybody is free to do the same thing. I'll probably end up making a small series on this dataset for [calmcode](https://calmcode.io) as well.

## Collaborative Nature 

Considering the topic I've asked some folks to help review/think along but everyone should feel free to pitch in. I've never been on the receiving end of salary bias and I am assuming that I have blind spots. Folks are free to send feedback via github issues but also to collaborate.

I hope this repository can function as an example of how to properly do similar analyses. This is why will ask folks to keep good coding practices in mind if they decide to contribute code.

## Related Work 

I'm not the only person who has looked at salary bias in tech. To those interested I can really recommend checking out [this blogpost](https://juliasilge.com/blog/salary-gender/) by Julia Silge. It uses the same dataset and explores different methods of modelling to quantify the effects on salary.
