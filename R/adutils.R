#' AD authentication
#'
#' \code{adauth} is a function to authenticate against the Active Directory.
#'
#' \code{user_email} and \code{password} are used to authenticate on \code{address}. Either host name or IP address can be specified.
#'
#' The response is a list of 2 elements: \code{is_authenticated} and \code{message}. \code{message} is \code{NULL} if \code{is_authenticated} is \code{TRUE}.
#'
#' @param address LDAP hostname or IP without protocol (ldap://)
#' @param user_email user email address
#' @param password password
#' @return response indicating whether authentication is successful
#' @export
#' @examples
#' \dontrun{
#'
#'adauth('hostname-or-ip', 'user_email', 'password')
#' }
adauth <- function(address, user_email, password) {
  path <- system.file('python', 'adauth.py', package = 'radhelper')
  command <- paste('python', path, '--address', address, '--user_email', user_email, '--password', password)

  response <- system(command, intern = TRUE)
  jsonlite::fromJSON(response)
}
