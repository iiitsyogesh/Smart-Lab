# Smart-Lab
This website is made using Django framework and is used for controlling various electrical appliances in home/lab via google firebase realtime database.
In order to use firebase databse with ESP32(microcontroller), the database rules were such that anyone with database url would be able to manipulate the data.
So instead of directly using front end (that would have exposed our dtatabase secrets) we used django to hide the secrets. 
This site uses http as well as websockets protocol.
