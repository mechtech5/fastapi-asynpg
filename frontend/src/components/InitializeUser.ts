import axios from "axios";
import { useEffect } from "react";
import { useStore } from "@/store";

const InitializeUser = () => {
  const setUser = useStore((state) => state.setUser);

  useEffect(() => {
    // Request interceptor
    axios.interceptors.request.use(
      (config) => {
        if (localStorage.accessToken) {
          config.headers["Authorization"] =
            "Bearer " + localStorage.accessToken;
        }
        return config;
      },
      (error) => {
        Promise.reject(error);
      }
    );

    // Response interceptor
    axios.interceptors.response.use(
      (response) => {
        return response;
      },
      function (error) {
        if (error.response.status === 401) {
          setUser({});
          localStorage.clear();
          return Promise.reject(error);
        }
        return Promise.reject(error);
      }
    );

    if (localStorage.accessToken) {
      setUser(localStorage.accessToken);
    } else {
      setUser(false);
    }
  }, [setUser]);

  return null;
};

export default InitializeUser;
