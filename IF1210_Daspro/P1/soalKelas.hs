--SOAL 1
isPos :: [Int] -> [Int]
isPos l
 | null l = l
 | head l > 0 = head l : isPos (tail l)
 | otherwise = isPos (tail l)

isNeg :: [Int] -> [Int]
isNeg l
 | null l = l
 | head l < 0 = head l : isNeg (tail l)
 | otherwise = isNeg (tail l)

isKabisat :: [Int] -> [Int]
isKabisat l
 | null l = l
 | (mod (head l) 100 == 0) && (mod (head l) 400 /= 0) = isKabisat (tail l)
 | mod (head l) 4 == 0 = head l : isKabisat (tail l)
 | otherwise = isKabisat (tail l)

 --SOAL 2
isEven :: Int -> Bool
isEven n = mod n 2 == 0

sumInteger :: Int -> Int -> (Int -> Bool) -> Int
sumInteger m n f
 | m > n = 0
 | otherwise = f m + sumInteger (m + 1) n f