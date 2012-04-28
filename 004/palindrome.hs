isPalindrome ::  Integer -> Bool
isPalindrome n = show n == reverse (show n)

main ::  IO ()
main = print $ maximum [prod | a <- [100..999], b <- [100..999], let prod = a * b, isPalindrome prod]
