const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL;

export const generateMatchReport = async (
  payload
) => {
  const response = await fetch(
    `${API_BASE_URL}/horoscope-match`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    }
  );

  return await response.json();
};