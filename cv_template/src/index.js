const today = new Date();

document.getElementById('sender_date').value=''.concat(today.toLocaleDateString("en-GB", {day: "2-digit"}),
                                                 ' ',
 												 today.toLocaleString('en-GB', { month: 'long' }),
												 ', ',
												 today.getFullYear());

