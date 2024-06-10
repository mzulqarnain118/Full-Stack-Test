<script>
  import { onMount } from 'svelte';
  import DOMPurify from 'dompurify';

  let cryptoData = [];
  let loading = true;
  let error = null;
  let page = 1;
  const perPage = 10;
  const apiUrl = process.env.VITE_API_URL;

  async function fetchCryptoData(page) {
    loading = true;
    error = null;
    try {
      const response = await fetch(`${apiUrl}/cryptos?page=${page}&per_page=${perPage}`);
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
      const data = await response.json();
      cryptoData = data.map(item => ({
        ...item,
        name: DOMPurify.sanitize(item.name),
        current_price: item.current_price
      }));
    } catch (err) {
      error = err.message;
    } finally {
      loading = false;
    }
  }

  onMount(() => {
    fetchCryptoData(page);
  });

  function nextPage() {
    page += 1;
    fetchCryptoData(page);
  }

  function prevPage() {
    if (page > 1) {
      page -= 1;
      fetchCryptoData(page);
    }
  }
</script>

<main>
  <header>
    <h1>Crypto Market Information</h1>
  </header>
  <section>
    {#if loading}
      <div class="loader"></div>
    {:else if error}
      <p class="error">{error}</p>
    {:else}
      <ul>
        {#each cryptoData as crypto}
          <li>
            <div class="crypto-item">
              <img src={crypto.image} alt={crypto.name} />
              <div class="crypto-details">
                <strong>{crypto.name}</strong>
                <p>${crypto.current_price.toFixed(2)}</p>
              </div>
            </div>
          </li>
        {/each}
      </ul>
      <div class="pagination">
        <button on:click={prevPage} disabled={page === 1}>Previous</button>
        <span>Page {page}</span>
        <button on:click={nextPage}>Next</button>
      </div>
    {/if}
  </section>
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
    background-color: #f5f5f5;
    font-family: Arial, sans-serif;
  }

  header {
    background-color: #4caf50;
    color: white;
    width: 100%;
    padding: 1em 0;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  h1 {
    margin: 0;
    font-size: 2em;
  }

  section {
    width: 100%;
    max-width: 800px;
    margin-top: 2em;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    background-color: white;
    margin-bottom: 1em;
    padding: 1em;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
  }

  .crypto-item {
    display: flex;
    align-items: center;
    width: 100%;
  }

  .crypto-item img {
    width: 50px;
    height: 50px;
    margin-right: 1em;
  }

  .crypto-details {
    display: flex;
    flex-direction: column;
  }

  .crypto-details strong {
    font-size: 1.2em;
  }

  .crypto-details p {
    margin: 0.5em 0 0;
    font-size: 1em;
    color: #333;
  }

  .loader {
    border: 8px solid #f3f3f3;
    border-top: 8px solid #4caf50;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .error {
    color: red;
    font-size: 1.2em;
  }

  .pagination {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 1em;
  }

  .pagination button {
    padding: 0.5em 1em;
    margin: 0 0.5em;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  .pagination button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }

  .pagination span {
    font-size: 1.2em;
  }
</style>
