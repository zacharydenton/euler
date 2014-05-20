import qualified Data.Set as Set

stringSet :: [Int] -> Set.Set String
stringSet = Set.fromList . map show . takeWhile (< 10000) . dropWhile (< 1000)

cyclic :: String -> String -> Bool
cyclic a b = drop 2 a == take 2 b

solve :: [Set.Set String] -> [[Int]]
solve sets = [map read [a, b, c, d, e, f] | a <- Set.toList $ head sets,
                                            b <- filter (cyclic a) $ concatMap Set.toList $ tail sets,
                                            let be = filter (Set.notMember b) $ tail sets,
                                            c <- filter (cyclic b) $ concatMap Set.toList be,
                                            let ce = filter (Set.notMember c) be,
                                            d <- filter (cyclic c) $ concatMap Set.toList ce,
                                            let de = filter (Set.notMember d) ce,
                                            e <- filter (cyclic d) $ concatMap Set.toList de,
                                            let ee = filter (Set.notMember e) de,
                                            f <- filter (cyclic e) $ concatMap Set.toList ee,
                                            cyclic f a]

main :: IO ()
main = print $ sum $ head $ solve figurates
    where figurates = map stringSet [[n*(n + 1) `quot` 2 | n <- [1..]],
                                     [n*n | n <- [1..]],
                                     [n*(3*n - 1) `quot` 2 | n <- [1..]],
                                     [n*(2*n - 1) | n <- [1..]],
                                     [n*(5*n - 3) `quot` 2 | n <- [1..]],
                                     [n*(3*n - 2) | n <- [1..]]]
