def h_index(n, citations):
  ans = []
  clist = list(citations)
  dp = [0]*(max(clist) + 1)
  # TODO: Complete the function to get the H-Index scores after each paper
  h = 0
  total = 0
  for i in range(n):
    if(clist[i] > h):
        dp[clist[i]] += 1
        total += 1
        total -= dp[h]
        dp[h] = 0
        if(total > h):
            h += 1
    ans.append(h)
  return ans


if __name__ == '__main__':
  t = int(input())

  for test_case in range(1, t + 1):
    n = int(input())                      # The number of papers
    citations = map(int, input().split()) # The number of citations for each paper
    h_index_scores = h_index(n, citations)
    print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))
