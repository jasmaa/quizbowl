
# Plan
  - Update game client-side
    - server calculates question progress and sends player proper state when player joins
    - client side will ping server for state, updates accordingly
    -  player will send answer and current time when buzzing, server will evaluate and change player/room state
	  - if wrong: server locks out  player
	  - if right: server awards points and becomes idle
	-  player can request next question
	  - if cond met (state is idle or overtime): go to next question

# Websocket

## request to server
message = {
	player_id:
	request_type:
	content:
}

Request types
  - ping
  - new_user
  - buzz_init
  - buzz_answer
  - next
  - set_name
  - get_answer
  - set_category
  - set_difficulty
  - reset_score
  - chat

## response from server
message = {
	response_type:
	game_state:
	current_time:
	start_time:
	end_time:
	buzz_start_time:
	current_question_content:{}
	category:
	room_category:
	score_dict:{}
}

## add to server
message = {
	response_type:
	player_id:
}

# Models

  - Room: room for  players to join
  
    - label (room name as url)
	- state: IDLE, PLAYING, CONTEST, etc?
	- players
	
	- current_question
	- start_time
	- end_time
	
	- buzz_player
	- buzz_start_time
	- buzz_end_time
	
  - Player: a player
    - player_id
	- room
    - name
	- score
	- locked_out
	- last_seen

  - Question: a stored question in db
    - category
    - points
	- content
	- answer
	- duration
	
  - Message: message sent by player to room
    - room
	- player
	
# Buzz timing notes
  - when a buzz ends, get the duration of buzz
    - start = start + buzz_duration
    - end = end + buzz_duration
  - during buzz
    - current_time = buzz_start_time