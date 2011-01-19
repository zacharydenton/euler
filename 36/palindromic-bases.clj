#!/usr/bin/env clojure
; The decimal number, 585 = 10010010012 (binary), is palindromic 
; in both bases.
;
; Find the sum of all numbers, less than one million, which are 
; palindromic in base 10 and base 2.
;
; (Please note that the palindromic number, in either base, may 
; not include leading zeros.)
(defn reversed [string]
  (apply str (reverse string)))

(defn palindrome? [string]
  (= string (reversed string)))

(defn palindrome-in-decimal-and-binary? [n]
  (and (palindrome? (Integer/toString n 2))
       (palindrome? (Integer/toString n))))

(println (reduce + (filter palindrome-in-decimal-and-binary? (range 1 1000000))))
