import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [deals, setDeals] = useState([]);
  
 useEffect(() => {
  console.log("API URL:", import.meta.env.VITE_API_BASE_URL);

  fetch(`${import.meta.env.VITE_API_BASE_URL}/api/deals`)
    .then((response) => {
      console.log("Status:", response.status);
      console.log("URL:", response.url);
      return response.json();
    })
    .then((data) => {
      console.log("Deals:", data);
      setDeals(data);
    });
}, []);

  
  return (
    <div className="app">
      <header className="header">
        <h1>North America Deal Radar</h1>
        <p>Find popular deals from North American official stores.</p>
      </header>

      <main className="deal-grid">
        {deals.map((deal) => (
          <div className="deal-card" key={deal.id}>

            <div className="deal-image">
				<div className="sale-badge">
					SALE
				</div>

				{deal.image_url ? (
					<img
						src={deal.image_url}
						alt={deal.name}
					/>
				) : (
					<div className="image-placeholder">
						Product Image
					</div>
					)}
			</div>

            <div className="deal-content">

              <div className="brand-name">
                 {deal.brand}
              </div>

              <h2>{deal.name}</h2>

              <div className="popular">
                🔥 Popular Style
              </div>

              <div className="price-row">
                <span className="current-price">
                  ${deal.current_price}
                </span>

                <span className="currency">
                  {deal.currency}
                </span>

                <span className="original-price">
                  ${deal.original_price}
                </span>
              </div>

              <div className="discount">
                {deal.discount}% OFF
              </div>

              <a
                className="view-button"
                href={deal.product_url}
                target="_blank"
                rel="noreferrer"
              >
                View Official Product
              </a>

            </div>
          </div>
        ))}
      </main>
    </div>
  );
}

export default App;