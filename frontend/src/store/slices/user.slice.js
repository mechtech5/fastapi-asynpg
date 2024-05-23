// import axios from "axios";
import { jwtDecode } from "jwt-decode";
import isEmpty from "lodash/isEmpty";
// import bcrypt from "bcryptjs";

export const createUserSlice = (set) => ({
  user: {},
  isAuthenticated: false,
  tokenError: "",
  setUser: (payload) => {
    try {
      const user = jwtDecode(payload.access_token);
      set((state) => ({
        user,
        isAuthenticated: !isEmpty(user),
        tokenError: "",
      }));
    } catch (error) {
      set({
        user: {},
        isAuthenticated: false,
        tokenError: payload ? "Invalid Token, please try again" : "",
      });
    }
  },
});
