#!/usr/bin/env clojure

(defn factorial [n]
  (if (or (= n 1) (= n 0)) 
    1 
    (* n (factorial (- n 1)))))

(println (apply + (map #(- (int %) 48) (str (factorial 100)))))
