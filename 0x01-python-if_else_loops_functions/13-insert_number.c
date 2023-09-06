#include "lists.h"
/**
 * insert_node - inserts a node in alist
 * @head: pointer to linked list
 * @number: value to be add
 *
 * Return: pointer to list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *bean, *temp;

	current = *head;
	bean = malloc(sizeof(listint_t));
	if (bean == NULL)
		return (NULL);
	bean->n = number;
	bean->next = NULL;
	if ((*head == NULL) || (current->n > number))
	{
		bean->next = *head;
		*head = bean;
		return (bean);
	}

	while (current->next != NULL)
	{
		if ((current->next->n) < number)
			current = current->next;
		else
		{
			temp = current->next;
			current->next = bean;
			bean->next = temp;
			return (bean);
		}
	}
	current->next = bean;
	return (bean);
}
