# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tbrizon <tbrizon@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 16:53:07 by tbrizon           #+#    #+#              #
#    Updated: 2019/11/05 17:52:45 by tbrizon          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from eval import Evaluator

if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coef = [1.0, 2.0, 1.0, 4.0, 0.5]

    a = Evaluator(words, coef)
    Evaluator.zip_evaluate(coef, words)
    Evaluator.enumerate_evaluate(coef, words)