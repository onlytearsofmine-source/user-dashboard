package helpers

import (
	"crypto/rand"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"errors"
	"log"
	"net/http"
	"time"

	"github.com/user-dashboard/models"
)

func GenerateUUID() (string, error) {
	b := make([]byte, 16)
	_, err := rand.Read(b)
	if err != nil {
		return "", err
	}
	return hex.EncodeToString(b), nil
}

func HashPassword(password string) (string, error) {
	hash := sha256.Sum256([]byte(password))
	return hex.EncodeToString(hash[:]), nil
}

func VerifyPassword(storedPassword, providedPassword string) bool {
	newHash, err := HashPassword(providedPassword)
	if err != nil {
		log.Println(err)
		return false
	}
	return newHash == storedPassword
}

func ParseJSONBody(w http.ResponseWriter, r *http.Request, target interface{}) error {
	err := json.NewDecoder(r.Body).Decode(target)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return err
	}
	return nil
}

func ValidateUser(user *models.User) error {
	if user.Username == "" || user.Email == "" || user.Password == "" {
		return errors.New("all fields are required")
	}
	return nil
}

func GetTimeNow() time.Time {
	return time.Now().UTC()
}