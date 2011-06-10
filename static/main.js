// main.js

$(function() {
    var rates = {};

    function get_rate (from, to, handler) {
	$('.error').html('');
	var key = from + to;
	if (typeof(rates[key]) === 'undefined') {
	    $.ajax({
		url: '/rate/' + from + '/' + to,
		success: function(data) {
		    rates[key] = new Number(data).valueOf();
		    handler(rates[key]);
		},
		error: function() {
		    $('.error').html(
			'An error occured while contacting the server');
		}
	    });	    
	}
	else {
	    handler(rates[key]);
	}
    }

    var active = null;

    function init_block (side, defcur, defamount) {
	var block = $('.' + side);
	var input = block.find('input[name=amount]');
	var symbol = null;
	var amount = null;

	var self = {
	    side: side,
	    amount: function () {
		return amount;
	    },
	    symbol: function () {
		return symbol;
	    }
	};

	var set_currency = function (newsym) {
	    symbol = newsym;
	    block.find('.symbol').html(symbol);
	    block.find('tr').removeClass('selected');
	    get_row(symbol).addClass('selected');
	};

	var get_row = function (symbol) {
	    return block.find('th:contains(' + symbol + ')').parent();
	};

	var scroll_to = function (symbol) {
	    var row = get_row(symbol);
	    var list = block.find('.currency-list');
	    var offset = 
		row.offset().top - 
		row.parent().offset().top - 
		(list.height() - row.height()) / 2;
	    list.scrollTop(offset);
	}

	var  recalculate = function () {
	    amount = '...';
	    input.val(amount);
	    var rate = get_rate(active.symbol(), symbol, function (rate) {
		if (rate == '') {
		    input.val('No data');
		}
		else {
		    amount = new Number(rate * active.amount()).toFixed(4);
		    input.val(amount);
		}
	    });
	}

	var propagate = function () {
	    $('.block').not(block).trigger('recalculate');
	}
	
	var currency_selected = function (symbol) {
	    set_currency(symbol);
	    if (self === active) {
		propagate();
	    }
	    else {
		recalculate();
	    }
	}

	var amount_changed = function () {
	    if (input.val() != amount) {
		amount = input.val();
		active = self;
		propagate();
	    }
	}

	input.bind('change keyup blur', amount_changed);
	block.bind('recalculate', recalculate);
	block.find('.currency-list tr').click(function() {
	    currency_selected($(this).find('th').html());
	});

	set_currency(defcur);
	scroll_to(defcur);
	if (typeof(defamount) !== 'undefined') {
	    input.val(new Number(defamount).toFixed(4));
	    amount_changed();
	}

	return self;
    }

    init_block('right', 'USD')
    init_block('left', 'CAD', 1.0);

    $('.left input[name=amount]').focus();
});
