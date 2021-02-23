import msgpack

# Take message an the message before and store it in memory
def format_message_sequence(message, message_before):
	messages = {}

	# Read msgpack file
	with open("messages.msgpack", "rb") as f:
		byte_data = f.read()

	messages = msgpack.unpackb(byte_data)

	# Append reply to before message if it is there, otherwise make a new entry
	try:
		messages[message_before].append(message)
	except:
		messages[message_before] = [message]

	print(messages)
	with open("messages.msgpack", "wb") as f:
		packed = msgpack.packb(messages)
		f.write(packed)
