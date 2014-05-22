import Data.List (nub)

crack :: [String] -> String
crack [] = []
crack xs = first : crack rest where
    heads = map head xs
    reject = nub $ map (!! 1) $ filter ((> 1) . length) xs
    first = head $ nub $ filter (`notElem` reject) heads
    rest = filter ((> 0) . length) $ map (\ys'@(y:ys) -> if y == first then ys else ys') xs

main :: IO ()
main = do
    str <- readFile "/home/zach/code/euler/079/keylog.txt"
    let attempts = lines str
    putStrLn $ crack attempts
