fivegon :: Int -> [[[Int]]]
fivegon n = [[[a, b, c], [d, c, e], [f, e, g], [h, g, i], [k, i, b]]
    | a <- [1..10],
      b <- filter (`notElem` [a]) [1..10],
      c <- filter (`notElem` [a, b]) [1..10],
      a + b + c == n,
      d <- filter (`notElem` [a, b, c]) [a..10],
      e <- filter (`notElem` [a, b, c, d]) [1..10],
      d + c + e == n,
      f <- filter (`notElem` [a, b, c, d, e]) [a..10],
      g <- filter (`notElem` [a, b, c, d, e, f]) [1..10],
      f + e + g == n,
      h <- filter (`notElem` [a, b, c, d, e, f, g]) [a..10],
      i <- filter (`notElem` [a, b, c, d, e, f, g, h]) [1..10],
      h + g + i == n,
      k <- filter (`notElem` [a, b, c, d, e, f, g, h, i]) [a..10],
      k + i + b == n]

main :: IO ()
main = putStrLn $ maximum [s | n <- [1..50], gon <- fivegon n, let s = concatMap show $ concat gon, length s == 16]
