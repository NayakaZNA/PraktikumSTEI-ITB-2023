module JamBangun where

-- Definition and Specification
jamBangun :: Int -> Int -> Int -> (Bool, Int, Int, Int)
{- Determines if the waking time exceeds the specified input time
   and calculates the time difference in hours, minutes, and seconds. -}

-- Integer inputs j, m, and d represent hours, minutes, and seconds respectively.

-- Implementation
jamBangun j m d =
    let
        -- Constants for wake-up time and input time
        wakeUpSeconds = 7 * 3600 + 45 * 60
        inputSeconds = j * 3600 + m * 60 + d
        
        -- Calculate the time difference in seconds
        timeDifferenceSeconds
            | wakeUpSeconds > inputSeconds = wakeUpSeconds - inputSeconds
            | otherwise = inputSeconds - wakeUpSeconds

        -- Calculate hours, minutes, and seconds
        hours = timeDifferenceSeconds `div` 3600
        minutes = (timeDifferenceSeconds `mod` 3600) `div` 60
        seconds = timeDifferenceSeconds `mod` 60
    in
        -- Return a tuple with a boolean indicating if wake-up time exceeds input time
        -- and the calculated hours, minutes, and seconds
        (wakeUpSeconds > inputSeconds, hours, minutes, seconds)
