import { render, waitFor, screen } from "@testing-library/svelte";
import App from "./App.svelte";
import fetchMock from "jest-fetch-mock";

fetchMock.enableMocks();

beforeEach(() => {
  fetch.resetMocks();
});

test("loads and displays crypto data", async () => {
  fetch.mockResponseOnce(
    JSON.stringify([
      { name: "Bitcoin", current_price: 45000, image: "bitcoin.png" },
      { name: "Ethereum", current_price: 3000, image: "ethereum.png" },
    ])
  );

  render(App);

  expect(screen.getByText("Loading...")).toBeInTheDocument();

  await waitFor(() =>
    expect(screen.queryByText("Loading...")).not.toBeInTheDocument()
  );
  await waitFor(() =>
    expect(screen.getByText("Crypto Market Information")).toBeInTheDocument()
  );

  expect(screen.getByText("Bitcoin")).toBeInTheDocument();
  expect(screen.getByText("$45000.00")).toBeInTheDocument();
  expect(screen.getByText("Ethereum")).toBeInTheDocument();
  expect(screen.getByText("$3000.00")).toBeInTheDocument();
});

test("handles error state", async () => {
  fetch.mockReject(() => Promise.reject("API is down"));

  render(App);

  expect(screen.getByText("Loading...")).toBeInTheDocument();

  await waitFor(() =>
    expect(screen.queryByText("Loading...")).not.toBeInTheDocument()
  );
  await waitFor(() =>
    expect(screen.getByText("Failed to fetch data")).toBeInTheDocument()
  );
});

test("sanitizes crypto names", async () => {
  fetch.mockResponseOnce(
    JSON.stringify([
      {
        name: '<script>alert("XSS")</script>',
        current_price: 45000,
        image: "bitcoin.png",
      },
    ])
  );

  render(App);

  await waitFor(() =>
    expect(screen.queryByText("Loading...")).not.toBeInTheDocument()
  );

  const cryptoName = screen.getByText('<script>alert("XSS")</script>', {
    selector: "strong",
  });
  expect(cryptoName).toBeInTheDocument();
});
