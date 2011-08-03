The grid can be expressed as [Pascal's Triangle](http://en.wikipedia.org/wiki/Pascal's_triangle):

<p style="text-align: center">
1<br />
1 1 <br />
1 <strong>2</strong> 1 <br />
1 3 3 1 <br />
1 4 <strong>6</strong> 4 1 <br />
1 5 10 10 5 1 <br />
1 6 15 <strong>20</strong> 15 6 1<br />
</p>

Note that the solution for a 1x1 grid is 2, a 2x2 grid is 6, and a 3x3 grid is 20.

If we compare these solutions to Pascal's Triangle, we see that they correspond to
the 1st element in the 2nd row, the 2nd element in the 4th row, and the 3rd element
in the 6th row, respectively. (Note that Pascal's Triangle is zero-indexed.)

The [binomial coefficient](http://en.wikipedia.org/wiki/Binomial_coefficient)
\\(\\binom {n} {k}\\) can be used to determine the \\(k\\)th element in the
\\(n\\)th row of Pascal's Triangle. Thus, we could express the aforementioned solutions as
\\(\\binom {2} {1}\\), \\(\\binom {4} {2}\\), and \\(\\binom {6} {3}\\), respectively.

Thus, a general solution for grids of size \\(x\\) is 

\\[routes = \\binom {2x} {x}\\].
