expansion :: [(Integer, Integer)]
expansion = iterate (\(n, d) -> (d, n + 2*d)) (1, 2)

main :: IO ()
main = print $ length [(n, d) | (n, d) <- take 1000 expansion, length (show (n + d)) > length (show d)]
