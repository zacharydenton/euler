#!/usr/bin/env clojure
(defn factorial [n]
  (if (or (= n 1) (= n 0)) 
    1 
    (* n (factorial (- n 1)))))

(defn digits [number]
  (map #(- (int %) 48) (str number))) 

(defn curious? [number]
  (and (= (apply + (map factorial (digits number))) number)
       (> (count (digits number)) 1)))

(println (reduce + (filter curious? (range 50000))))
