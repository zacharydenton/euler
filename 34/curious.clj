#!/usr/bin/env clojure
; 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
;
; Find the sum of all numbers which are equal to the sum of the factorial of their digits.
;
; Note: as 1! = 1 and 2! = 2 are not sums they are not included.
(defn factorial [n]
  (if (or (= n 1) (= n 0)) 
    1 
    (* n (factorial (- n 1)))))

(defn digits [number]
  ; convert the number to a string,
  ; and convert each char to an int.
  ;
  ; subtract 48 because casting a char
  ; to an int returns the ASCII
  ; representation of that char.
  (map #(- (int %) 48) (str number))) 

(defn curious? [number]
  ; if the sum of the factorials of the digits
  ; is equal to the number
  ; itself, then it is a curious number.
  (and (= (apply + (map factorial (digits number))) number)
       (> (count (digits number)) 1)))


(time (println (reduce + (filter curious? (range 50000)))))
