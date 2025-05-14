# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].


def count_positives_sum_negatives(lst)
  positive_count = 0
  negative_sum = 0

  if lst == [] || lst == nil
    return []
  end

  lst.each do |num|
    if num > 0
      positive_count += 1
    elsif num < 0
      negative_sum += num
    end
  end

  return [positive_count, negative_sum]

  ## Alternative solution:
  # return [] if lst.empty?

  # positives, negatives = lst.partition(&:positive?)

  # [positives.count, negatives.sum]
end

# Example
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
p count_positives_sum_negatives(lst)
# Answer should be [10, -65]