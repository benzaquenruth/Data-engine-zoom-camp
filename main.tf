terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.17.0"
    }
  }
}

provider "google" {
  project = "celtic-science-485518-g9"
  region  = "us-central1"
}

resource "google_storage_bucket" "demo_bucket" {
  name          = "celtic-science-485518-g9-terra-bucket"
  location      = "US"
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
