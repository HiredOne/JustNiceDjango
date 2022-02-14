const firebaseConfig = {
    apiKey: "AIzaSyCG4pAXNIr1sjk-PbEwIkRt7a9AWPZdK0U",
    authDomain: "democpp-2577e.firebaseapp.com",
    projectId: "democpp-2577e",
    storageBucket: "democpp-2577e.appspot.com",
    messagingSenderId: "765444663504",
    appId: "1:765444663504:web:77474ac5fc75fb2d0ed6d5"
  };
  // Initialise Firebase
  firebase.initializeApp(firebaseConfig);

  var db = firebase.firestore();

  // ------------ Save to Firestore ------------ //
  function savetofs() {

    var a = document.getElementById("coin1").value;
    var b = document.getElementById("ticker1").value;
    var c = document.getElementById("buy1").value;
    var d = document.getElementById("quant1").value;

    alert("Saving your data for Coin: " + a);

    db.collection("Portfolio").doc(a).set({
        Coin : a,
        Ticker : b,
        Buy_Price : c,
        Buy_Quantity : d
    })
    .then((docRef) => {
        console.log(docRef);
        window.location.reload();
    })
    .catch((error) => {
        console.error("Error adding document: ", error);
    })
  }

  // ------------ Display Profit Losses ------------ //
  async function display() {
      let z = await db.collection("Portfolio").get();
      let ind = 1;
      var tp = 0;

      z.forEach((docs) => {
          let yy = docs.data();
          let table = document.getElementById("cppTable");
          let row = table.insertRow(ind);

          let coin = (yy.Coin);
          let price = (yy.Buy_Price);
          let quantity = (yy.Buy_Quantity);
          let ticker = (yy.Ticker);

          let cell1 = row.insertCell(0); let cell2 = row.insertCell(1); let cell3 = row.insertCell(2);
          let cell4 = row.insertCell(3); let cell5 = row.insertCell(4); let cell6 = row.insertCell(5);
          let cell7 = row.insertCell(6); let cell8 = row.insertCell(7);

          cell1.innerHTML = ind; cell2.innerHTML = coin; cell3.innerHTML = ticker; cell4.innerHTML = price; cell5.innerHTML = quantity;
          cell6.innerHTML = 0; cell7.innerHTML = 0;

          cell7.className = "profits";

          var bu = document.createElement("button");
          bu.className = "bwt";
          bu.id = String(coin);
          bu.innerHTML = "Delete";
          bu.onclick = function() {
              deleteInstrument2(coin)
          }
          cell8.appendChild(bu);

          val(ticker)

          async function val(ticker) {
            let binance = new ccxt.binance();
            let z = await binance.fetch_ohlcv(ticker, "5m");
            cell6.innerHTML = z[499][4];
            cell7.innerHTML = Math.round(quantity * (-parseFloat(price) + parseFloat(cell6.innerHTML)));
            tp = tp + parseFloat(cell7.innerHTML);
            document.getElementById("totalProfit").innerHTML = ("Your Total Profit is : $" + String(tp));
        }
        ind += 1;
      })
  }

  display();

  // ------------ Delete Instruments ------------ //

  function deleteInstrument2(coin) {
      let x = coin;
      alert("You are going to delete: " + x);
      console.log(x);
      db.collection("Portfolio").doc(x).delete().then(() => {
          console.log("Document successfully deleted!", x);
          window.location.reload()
      })
      .catch((error) => {
          console.error("Error removing document: ", error);
      })
  }

  // ------------ END ------------ //