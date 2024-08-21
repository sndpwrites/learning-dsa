# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
import matplotlib.pyplot as plt

def unique1(S):
  """Return True if there are no duplicate elements in sequence S."""
  for j in range(len(S)):
    for k in range(j+1, len(S)):
      if S[j] == S[k]:
        return False              # found duplicate pair
  return True                     # if we reach this, elements were unique

def unique2(S):
  """Return True if there are no duplicate elements in sequence S."""
  temp = sorted(S)                # create a sorted copy of S
  for j in range(1, len(temp)):
    if S[j-1] == S[j]:
      return False                # found duplicate pair
  return True                     # if we reach this, elements were unique

def analyze_algorithm(algorithm, input_sizes):
    running_times = []
    for n in input_sizes:
        S = range(1, n+1)
        start_time = time.time()
        algorithm(S)
        end_time = time.time()
        running_time = end_time - start_time
        running_times.append(running_time)
    return running_times

input_sizes = [10, 100, 1000, 10000]
unique1_times = analyze_algorithm(unique1, input_sizes)
unique2_times = analyze_algorithm(unique2, input_sizes)

plt.plot(input_sizes, unique1_times, label='unique1')
plt.plot(input_sizes, unique2_times, label='unique2')
plt.xlabel('Input Size')
plt.ylabel('Running Time (seconds)')
plt.title('Uniqueness Algorithms')
plt.legend()
plt.savefig('./runtime_analysis_uniqueness.png')