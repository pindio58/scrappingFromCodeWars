# from bs4 import BeautifulSoup
# markup = '''<div class="markdown prose max-w-5xl mx-auto" id="description">
#     <p>There is an array with some numbers. All numbers are equal except for one. Try to find it!</p>
#     <pre><code class="language-javascript"><span class="cm-variable">findUniq</span>([ <span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span> ]) <span class="cm-operator">===</span> <span class="cm-number">2</span>
# <span class="cm-variable">findUniq</span>([ <span class="cm-number">0</span>, <span class="cm-number">0</span>, <span class="cm-number">0.55</span>, <span class="cm-number">0</span>, <span class="cm-number">0</span> ]) <span class="cm-operator">===</span> <span class="cm-number">0.55</span>
# </code></pre>
#     <pre style="display: none;"><code class="language-swift"><span class="cm-variable">findUniq</span><span class="cm-punctuation">(</span><span class="cm-punctuation">[</span> <span class="cm-number">1</span><span class="cm-punctuation">,</span> <span class="cm-number">1</span><span class="cm-punctuation">,</span> <span class="cm-number">1</span><span class="cm-punctuation">,</span> <span class="cm-number">2</span><span class="cm-punctuation">,</span> <span class="cm-number">1</span><span class="cm-punctuation">,</span> <span class="cm-number">1</span> <span class="cm-punctuation">]</span><span class="cm-punctuation">)</span> <span class="cm-operator">=</span><span class="cm-operator">=</span> <span class="cm-number">2</span>
# <span class="cm-variable">findUniq</span><span class="cm-punctuation">(</span><span class="cm-punctuation">[</span> <span class="cm-number">0</span><span class="cm-punctuation">,</span> <span class="cm-number">0</span><span class="cm-punctuation">,</span> <span class="cm-number">0.55</span><span class="cm-punctuation">,</span> <span class="cm-number">0</span><span class="cm-punctuation">,</span> <span class="cm-number">0</span> <span class="cm-punctuation">]</span><span class="cm-punctuation">)</span> <span class="cm-operator">=</span><span class="cm-operator">=</span> <span class="cm-number">0.55</span>
# </code></pre>
#     <pre style="display: none;"><code class="language-ruby"><span class="cm-variable">find_uniq</span>([ <span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span> ]) <span class="cm-operator">==</span> <span class="cm-number">2</span>
# <span class="cm-variable">find_uniq</span>([ <span class="cm-number">0</span>, <span class="cm-number">0</span>, <span class="cm-number">0</span><span class="cm-operator">.</span><span class="cm-number">55</span>, <span class="cm-number">0</span>, <span class="cm-number">0</span> ]) <span class="cm-operator">==</span> <span class="cm-number">0</span><span class="cm-operator">.</span><span class="cm-number">55</span>
# </code></pre>
#     <pre style="display: none;"><code class="language-python"><span class="cm-variable">find_uniq</span>([ <span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span> ]) <span class="cm-operator">==</span> <span class="cm-number">2</span>
# <span class="cm-variable">find_uniq</span>([ <span class="cm-number">0</span>, <span class="cm-number">0</span>, <span class="cm-number">0.55</span>, <span class="cm-number">0</span>, <span class="cm-number">0</span> ]) <span class="cm-operator">==</span> <span class="cm-number">0.55</span>
# </code></pre>
#     <pre style="display: none;"><code class="language-java"><span class="cm-variable">Kata</span>.<span class="cm-variable">findUniq</span>(<span class="cm-keyword">new</span> <span class="cm-type">double</span>[]{ <span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span> }); <span class="cm-comment">// =&gt; 2</span>
# <span class="cm-variable">Kata</span>.<span class="cm-variable">findUniq</span>(<span class="cm-keyword">new</span> <span class="cm-type">double</span>[]{ <span class="cm-number">0</span>, <span class="cm-number">0</span>, <span class="cm-number">0.55</span>, <span class="cm-number">0</span>, <span class="cm-number">0</span> }); <span class="cm-comment">// =&gt; 0.55</span>
# </code></pre>
#     <pre style="display: none;"><code class="language-haskell"><span class="cm-variable">getUnique</span> [<span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span>, <span class="cm-number">2</span>, <span class="cm-number">1</span>, <span class="cm-number">1</span>] <span class="cm-comment">-- Result is 2</span>
# <span class="cm-variable">getUnique</span> [<span class="cm-number">0</span>, <span class="cm-number">0</span>, <span class="cm-number">0.55</span>, <span class="cm-number">0</span>, <span class="cm-number">0</span>] <span class="cm-comment">-- Result is 0.55</span>
# </code></pre>
#     <pre style="display: none;"><code class="language-fsharp"><span class="cm-variable">findUniq</span>([ <span class="cm-number">1</span>; <span class="cm-number">1</span>; <span class="cm-number">1</span>; <span class="cm-number">2</span>; <span class="cm-number">1</span>; <span class="cm-number">1</span> ]) <span class="cm-operator">=</span> <span class="cm-number">2</span>
# <span class="cm-variable">findUniq</span>([ <span class="cm-number">0</span>; <span class="cm-number">0</span>; <span class="cm-number">0.55</span>; <span class="cm-number">0</span>; <span class="cm-number">0</span> ]) <span class="cm-operator">=</span> <span class="cm-number">0.55</span>
# </code></pre>
#     <p>It’s guaranteed that array contains at least 3 numbers.</p>
#     <p>The tests contain some very huge arrays, so think about performance.</p>
#     <p>This is the first kata in series:</p>
#     <ol>
#         <li>Find the unique number (this kata)</li>
#         <li><a href="https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3" target="_blank">Find the unique string</a>
#         </li>
#         <li><a href="https://www.codewars.com/kata/5862e0db4f7ab47bed0000e5" target="_blank">Find The Unique</a></li>
#     </ol>
# </div>'''
# soup = BeautifulSoup(markup,features='html.parser')

# # for pre in soup.find_all('pre'):
# #     if 'python' not in pre.code.attrs['class'][0]:
# #         pre.decompose()
# # print(soup)
# # soup.has_attr
# # print(len(soup.attrs))
# # for pre in soup.find_all('pre'):
# #     print(pre.code.has_attr('class'))

# print(len(soup.find_all('pre')))

# for pre in soup.find_all('pre'):
#     print(pre.code.has_attr('class'))


import pathlib
import sys
COOKIESFILE=str(pathlib.Path(__file__).parent.resolve())
COOKIESFILE=COOKIESFILE+'cookies.csv'
print(COOKIESFILE)