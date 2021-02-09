import math


def get_maximum_spacing(line_comment, total_width, title):
	""" Returns the maximum possible spacing on each side of the title. """
	return math.floor((total_width - (len(line_comment) + len(title)))/2)


def get_side_separator_length(maximum_spacing, preferred_spacing):
	""" Returns the side separator length that is actually used. """
	# print(f"maximum: {maximum_spacing}, preferred: {preferred_spacing}")
	assert maximum_spacing > preferred_spacing  # fix later

	return maximum_spacing - preferred_spacing


def is_uneven(number):
	return number/2 != number//2


def generate(line_comment, separator, total_width, rows, title, 
			 preferred_spacing):
	""" Generates and returns a separator. """

	separator_line = line_comment + "".join(
		[separator for elem in range(total_width - len(line_comment))]
	) + "\n"

	above_and_below_separators = "".join(
		[separator_line for elem in range(math.ceil(rows/2))]
	)

	maximum_spacing = get_maximum_spacing(line_comment, total_width, title)

	side_separator_length = get_side_separator_length(
		maximum_spacing, 
		preferred_spacing
	)

	side_separator = separator * side_separator_length
	side_spacing = " " * preferred_spacing

	# compensate with extra separator symbol if one of len(title) and
	# total_width is uneven and not the other:
	compensate_uneven_title \
		= separator if is_uneven(len(title)) and not is_uneven(total_width) else ""

	compensate_uneven_length \
		= separator if is_uneven(total_width) and not is_uneven(len(title)) else ""

	result = ""
	result += above_and_below_separators
	result += f"{line_comment}{side_separator}{side_spacing}"
	result += f"{title}{side_spacing}{side_separator}"
	result += f"{compensate_uneven_title}{compensate_uneven_length}\n"
	result += above_and_below_separators	
	return result

print(
	generate("//", "#", 80 , 3, "abc", 5)
)
print(
	generate("//", "#", 80 , 3, "abcd", 5)
)
print(
	generate("//", "#", 81 , 3, "abc", 5)
)
print(
	generate("//", "#", 81 , 3, "abcd", 5)
)