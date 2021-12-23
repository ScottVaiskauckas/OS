var deck_object = $('#deck-json').data();
var deck = deck_object['deck']

function DrawACard()
{ 
  var random_int = Math.floor(Math.random() * deck.length);
  var card = deck[random_int];
  $('#deck-text').html(card);
}