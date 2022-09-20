#include "lists.h"

/**
 * check_cycle - function checks to see if a list is in an
 * endless loop or cycle
 * @list: pointer par
 * Return: 0 if !cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *doub = list;
	listint_t *reg = list;

	if (list == NULL)
		return (0);

	while (doub && doub->next)
	{
		reg = reg->next;
		doub = doub->next->next;

		if (reg == doub)
			return (1);
	}
	return (0);
}
