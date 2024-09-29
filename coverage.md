Statement Coverage - this is also known as line coverage. Statement coverage measures the percentage of the code statements that has been tested. In this test coverage approach, the main goal is to test 100% of LINES, without the decision points being the main focus. For example, suppose there is a function with ten lines of code. During testing, if the tester executes all ten lines at least once, the
statement coverage reaches 100%. However, if he executes only eight out of the ten lines, the statement coverage becomes 80%.

Branch Coverage -  branch coverage measures percentage of branches (decisions) tested. In this test coverage approach, the main goal is to test all branches, by going through all decision points with different outcomes (true and false). For example, suppose there is a function with an if-else statement. The function has two possible branches, one for the if condition and another for the else condition. During testing, the tester achieves 100% branch coverage if he executes both branches at least once.

Predicate Coverage - this one is similar to the branch coverage but differs when there is complex statements on the decision points. It tests all possible combinations of the conditions inside a complex decision point. For example, suppose there is an if statement like: x > 5 && y < 10. Branch coverage will test this one based on overall outcome (true and false). But predicate coverage requires delving deeper and considering all possible combinations:
x > 5 is T and y < 10 is T
x > 5 is T and y < 10 is F
x > 5 is F and y < 10 is T
x > 5 is F and y < 10 is F