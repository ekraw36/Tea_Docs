# Statistical Analysis Glossary
This document provides basic explanations for the key parts of statistical analysis. Each section provides a general overview of the function of the element, and the different varieties of that element that are supported by Tea. To learn more about using these elements within Tea, refer to Tea’s Task Documentation.

---
## Variables
Variables represent the pieces of information measured or observed in a study. Tea uses variable definitions to understand what kind of data you have and which statistical tests are appropriate for your data.

**Variable Data Types**
Tea supports four varieties of variable data types. These correspond to standard measurement levels in statistics and determine which comparisons and tests are valid.

- ***Nominal:*** The data can be sorted into categories with no inherent ordering within them. Tea treats each category as distinct but unordered.
> A medical patient’s pain can be organized into headache, stomachace, back pain, etc.

- ***Ordinal:*** The data can be sorted into categories with an internal order, but without consistent spacing between levels. Tea preserves order information but does not assume equal intervals.
> A medical patient’s pain level can be organized into none, mild, moderate, severe. But the difference between mild and moderate is not guaranteed to be equal to the difference between moderate and severe.

- ***Interval:*** The data can be sorted into numerical values without a true “zero point”/zero DOES NOT represent the absence of data. Tea allows arithmetic comparisons but does not interpret ratios.
> A medical patient’s pain level can be organized on a scale of 0 to 10. Differences are meaningful (7 is greater pain than 5) but comparisons (10 is twice as much pain as 5) are not valid interpretations.

- ***Ratio:*** The data can be sorted into numerical values with a true “zero point” and consistent units. Zero DOES represent an absence of data being measured.Tea supports all numeric operations, including ratios and proportional reasoning.
> A medical patient’s pain can be measured by the firing rate of their pain stimuli nerves within their nervous system. Data is measured in milliVolts (mV). 0 mV means “no signal” and 3.2 mV is twice 1.6 mV.

## Study Designs
The study design describes how the data was collected and what kind of claims around cause/effect and association are appropriate.

***Experiment:*** A design where the researcher directly manipulates one or more variables and keeps all non-relevant variables the same across all tests.

  - *Independent Variable:* The variable manipulated by researchers. It is thought to influence or predict the dependent variable.
  > A researcher feeds one group of rats a vegetarian diet and another group an omnivore diet and records their energy levels throughout the day. The diet of the rats is the independent variable.

  - *Dependent Variable:* The outcome of the experiment being measured. The experiment tests how this variable changes (or doesn’t change) when another variable is being manipulated by the researcher.
  > A researcher feeds one group of rats a vegetarian diet and another group an omnivore diet and records their energy levels throughout the day. The energy levels of the rats is the dependent variable.

***Observational Study:*** A design where variables are measured by researchers in a natural environment without intervention.

  - *Contributor Variable:* Very similar to the independent variable in an experiment. A variable that may contribute to variation in the outcome variable but is not experimentally controlled by the researcher.
  - *Outcome Variable:* Very similar to the dependent variable in an experiment. The outcome of the study being measured. Variance in this measurement is thought to be associated with the contributor variable.
	
## Hypotheses
Hypotheses describe the relationship between variables that you expect to test. Tea uses these to determine which statistical tests are valid to use on your data and how to interpret results.

- ***One-sided comparison between groups:*** Tests whether one group tends to have a greater or smaller amount of a defined value than another group.
> Participants who receive the drug will have lower pain levels than those who receive the placebo.

- ***Two-sided comparisons:*** Tests whether groups differ from each other, without specifying which is larger.
> The pain level will differ between the drug group and the placebo group

- ***Partial orders:*** Specify an ordering among multiple groups (A < B < C) without requiring exact numerical differences
> The pain levels of the placebo group will be greater than the pain levels of the low dosage group, which will be greater than the pain levels of the high dosage group.

- ***Positive linear relationship:*** Tests whether increases in one numeric variable are associated with increases in another.
> The higher dosage of the drug is associated with a higher nausea level

- ***Negative linear relationship:*** Tests whether increases in one numeric variable are associated with decreases in another.
> The higher dosage of the drug is associated with a lower pain level.

- ***Null hypothesis:*** The default assumption that there is no effect, difference, or relationship between the variables. Tea uses this as a baseline for statistical testing.
> There is no difference in pain level between the drug and placebo groups.

## Assumptions
Assumptions describe statistical properties that you believe are true in your data. These are optional to include in your analysis in Tea. Tea checks these assumptions when selecting tests and interpreting results.
			
- ***Normal distribution:*** Assumes a variable follows a bell-shaped distribution. Required for many parametric tests.

- ***Normal distribution within the categories of another variable:*** Assumes each group is normally distributed. Important for ANOVA and t-tests.

- ***Log normal distribution:*** Assumes the logarithm of the variable is normally distributed. Useful for skewed/unbalanced data.

- ***Equal variance:*** Assumes groups have similar variability. Required for tests like the independent samples t-test.

- ***Type I (False Positive) Error Rate / Alpha value:*** Sets the significance threshold for the results of tests. Tea uses this to decide whether to reject the null hypothesis.

## Possible Tests
Tea supports a variety of statistical tests that each test for a different result. Tea automatically selects the most appropriate test from a library of statistical tests based on your variables, hypotheses, and assumptions. Each test can be organized into four categories:
	
- **Group Comparison Tests**
These tests evaluate whether two or more groups differ on a chosen outcome. They answer questions like “Does the drug reduce pain compared to the placebo?”

- **Correlation Tests**
These tests evaluate whether two variables change together in a consistent pattern. They quantify the strength and direction of a relationship between two variables. They answer questions like “Is an increase in drug dosage associated with a change in pain level?”

- **Model-based tests**
These tests evaluate structured relationships involving multiple predictors, interactions, and other complex designs. They answer questions like “Does dosage reduce pain even after controlling for age?”

- **Rank-based / Nonparametric alternatives**
These tests evaluate differences or relationships between variables without assuming normality or equal variance. They answer the same questions as the tests above but work on ranked data instead of raw values.
	
## Results
Tea returns structured results containing key outputs of the selected statistical test.

- ***test_statistic:*** The numeric value summarizing the evidence against the null hypothesis.
- ***p_value:*** The probability of observing results at least as extreme as your data if the null hypothesis were true. If p-value is very low, then it is very unlikely that the null hypothesis is true.
- ***adjusted_pvalue:*** A p-value corrected for multiple comparisons when applicable. Depends on the hypothesis and selected test.
- ***alpha:*** The significance threshold used to evaluate the p-value. If the p-value is less than the alpha, then the null hypothesis is rejected and the results are deemed statistically significant.
- ***dof:*** Degrees of Freedom, representing the amount of independent information available for estimating variability.
- ***Cohen’s d:*** A standardized effect size measuring the magnitude of a difference between groups.
- ***A12:*** A nonparametric effect size representing the probability that a randomly chosen value from one group exceeds the value of another.
		



