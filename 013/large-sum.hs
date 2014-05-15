main :: IO ()
main = do
        str <- readFile "/home/zach/code/euler/013/digits.txt"
        putStrLn $ take 10 $ show $ sum $ map read $ lines str
