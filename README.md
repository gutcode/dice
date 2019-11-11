 <div class="description user_content student-version"><p>Let's play dice! The traditional die is a cube. Each of its six faces shows a different number of dots from 1 to 6. Dice are used to produce results from 1 through 6. When a die is thrown (or rolled) and the die comes to rest, the face of the die that is uppermost provides the value of the throw. If an unbiased die is thrown, each value from 1 to 6 is equally likely.</p>
<p>Your programming task is related to the analysis of sequences produced by rolling a die.</p>
<p>Create a program named<span> </span><span><strong>Dice</strong></span><span> </span>to solve the following exercises. The input of the program is a so-called trial, i.e. a sequence of the rolled results. This input must be read from the<span> </span><strong><span>standard input</span></strong>. The first line of the input contains a single integer N, indicating the number of throws<span>1<N<1000000</span>. The second line of the input contains exactly N characters, each character is a digit from 1 to 6. For example, the input can be as follows:</p>
<pre>8<br>32646135</pre>
<p>The output of the program should be written to the<span> </span><strong><span>standard output</span></strong>. There are 3 exercises you are expected to solve. The output should contain exactly 3 lines: the<span> </span><strong><em>i</em></strong>th line in the output is the solution to exercise<span> </span><strong><em>i</em></strong><span>.</span></p>
<p>--------------------------------------------------------------------------------</p>
<h3>Exercises</h3>
<h4><span>Exercise 1</span></h4>
<p>How many times did it occur in the trial, that exactly two 6s were rolled after each other? For example, in sequence 5<span>66</span>111<span>666</span>2<span>66</span>3441<span>6</span><span> </span>it occurred twice, that exactly two 6s were thrown after each other.</p>
<h4><span>Exercise 2</span></h4>
<p>Find the length of the longest subsequence of successive rolls, in which the value 6 does not occur. (This number can be zero, if only 6s were thrown.) For example, in the trial 66<span>423</span>6<span>12345</span>6<span>54</span><span> </span>the longest subsequence of successive rolls in which the value 6 does not occur is 12345. Its length is 5. </p>
<h4><span>Exercise 3</span></h4>
<p>We shall call a sequence of successive rolls in the trial a<span> </span><span>lucky series</span>, if the sequence contains only 5s and 6s. For example 6556665 is a lucky series, with a length of 7.<br>Find out, which is the<span> </span><span>most frequent length</span><span> </span>for lucky series. If there are more than one "most frequent" lucky series lengths, print the longest. If there are no lucky series in the trial, print zero.</p>
<p>Be aware. We are not interested in the most frequent lucky series. The four lucky series 656, 555, 556 and 666 are equivalent for us, all of them are lucky series of length three. We are looking for the most frequent length of lucky series.</p>
<p>For example, in trial<span> </span><span>55</span>33<span>66</span>1<span>656</span>, the series 656 is the longest lucky series. But there is only one lucky series of lenght three in the trial. 55 and 66 are also lucky series. This is why the correct answer is 2. In trial 4<span>56</span>11<span>65</span>13<span>656</span>124<span>566</span><span> </span>both the lucky series with length of 2 and 3 occur twice, there is a tie between them. Now the length of the longest (that is 3) should be printed. Examples example1 and example2 are aimed to make this situation clear.<span></span> </p>
<p>--------------------------------------------------------------------------------</p>
<h3>Examples</h3>
<p>We provide three simple examples to clarify the exercises. Test your solution with other, larger examples as well!</p>
<h4><span>Example 1</span></h4>
<p>Sample input:</p>
<pre>9<br>616161666</pre>
<p>Sample output:</p>
<pre>0<br>1<br>1</pre>
<h4><span>Example 2</span></h4>
<p>Sample input:</p>
<pre>18<br>456116513656124566</pre>
<p>Sample output:</p>
<pre>1<br>4<br>3</pre>
<h4><span>Example 3</span></h4>
<p>Sample input:</p>
<pre>17<br>56611166626634416</pre>
<p>Sample output:</p>
<pre>2<br>4<br>3</pre></div>

