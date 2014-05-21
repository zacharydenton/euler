All square roots are periodic when written as continued fractions and can be written in the form:

$$\sqrt{N} = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \dots}}}$$

For example, let us consider $\sqrt{23}$:

$$\sqrt{23} = 4 + \sqrt{23} - 4 = 4 + \frac{1}{\frac{1}{\sqrt{23} - 4}} = 4 + \frac{1}{1 + \frac{\sqrt{23} - 3}{7}}$$

If we continue we would get the following expansion:

$$\sqrt{23} = 4 + \cfrac{1}{1 + \cfrac{1}{3 + \cfrac{1}{1 + \cfrac{1}{8 + \dots}}}}$$

The sequence is repeating. For conciseness, we use the notation $\sqrt{23} = [4;(1,3,1,8)]$, to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

$$
\begin{aligned}
\sqrt{2} &= [1;(2)], \, \mathrm{period}=1 \\
\sqrt{3} &= [1;(1,2)], \, \mathrm{period}=2 \\
\sqrt{5} &= [2;(4)], \, \mathrm{period}=1 \\
\sqrt{6} &= [2;(2,4)], \, \mathrm{period}=2 \\
\sqrt{7} &= [2;(1,1,1,4)], \, \mathrm{period}=4 \\
\sqrt{8} &= [2;(1,4)], \, \mathrm{period}=2 \\
\sqrt{10} &= [3;(6)], \, \mathrm{period}=1 \\
\sqrt{11} &= [3;(3,6)], \, \mathrm{period}=2 \\
\sqrt{12} &= [3;(2,6)], \, \mathrm{period}=2 \\
\sqrt{13} &= [3;(1,1,1,1,6)], \, \mathrm{period}=5 \\
\end{aligned}
$$

Exactly four continued fractions, for $N \leq 13$, have an odd period.

How many continued fractions for $N \leq 10000$ have an odd period?

